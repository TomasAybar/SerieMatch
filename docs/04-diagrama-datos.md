# Conexión entre estructuras

Este diagrama muestra cómo se conectan los datos y las estructuras de SerieMatch: de dónde salen los datos, qué estructura se construye con ellos y qué opción del menú usa cada una.

## Diagrama

```
                 datos/series.json
                        │  Catalogo.cargar_datos()
                        ▼
                Catalogo (lista de Serie)
     ┌──────────┬───────┴──────┬──────────────┐
     ▼          ▼              ▼              ▼
  ArbolAVL  ArbolGeneral    MaxHeap      GrafoSeries
  (título)  (Catálogo →    (puntuación)  (géneros
             Género →                     compartidos)
             Serie)
     │          │              │              │
     └──────────┴──────┬───────┴──────────────┘
                       ▼
                   ConsolaUI  ◄──── GestorFavoritos ◄──► datos/favoritos.txt
                 (menú 0–10)
```

## Cómo se conectan

1. **Una sola fuente de datos.** `main.py` carga `datos/series.json` una vez con `Catalogo.cargar_datos()` y obtiene la lista de objetos `Serie`.
2. **Todas las estructuras se construyen al iniciar** a partir de esa misma lista. Cada estructura guarda referencias a los mismos objetos `Serie`, no copias.
3. **La interfaz recibe todas las estructuras** (`ConsolaUI`) y cada opción del menú usa la que le corresponde.
4. **Favoritos es independiente del catálogo en memoria:** `GestorFavoritos` lee y escribe `datos/favoritos.txt`, y usa el catálogo solo para mostrar los datos de cada ID guardado.

## Qué guarda cada estructura

| Estructura | Archivo | Qué guarda | Clave / criterio | Opción del menú |
|---|---|---|---|---|
| Lista (`Catalogo`) | `modelos/catalogo.py` | Todas las series | Orden del JSON | 3. Ver series · 6. Filtrar por género |
| Árbol AVL | `estructuras/avl.py` | Cada serie en un nodo | Título en minúsculas | 4. Buscar serie por título |
| Árbol general | `estructuras/arbol_general.py` | Raíz → géneros → títulos | Jerarquía Catálogo → Género → Serie | 7. Explorar categorías |
| MaxHeap | `estructuras/heap.py` | Todas las series | Puntuación (mayor en la raíz) | 8. Ranking de series |
| Grafo | `estructuras/grafo.py` | ID de serie → IDs vecinos | Comparten al menos un género | 9. Series relacionadas |
| Archivo de favoritos | `modelos/favoritos.py` | IDs de series, uno por línea | Orden en que se agregaron | 10. Favoritos |

El diagrama de clases completo está en la [documentación final](11-documentacion-final.md#62-diagrama-de-clases-final).
