# Diagrama de clases — boceto inicial (TP0)

> Estado: boceto TP0. Se actualiza en entregas posteriores con la implementación real y la incorporación de estructuras de datos más complejas vistas en la materia.

```mermaid
classDiagram
    class Serie {
        -titulo: str
        -generos: list
        -duracion_min: int
        -puntuacion: float
        -plataforma: str
        -sinopsis: str
        +get_titulo() str
        +mostrar_info() str
    }

    class Catalogo {
        -series: list
        +cargar_datos(ruta_archivo)
        +buscar_por_titulo(titulo) Serie
        +obtener_ranking() list
        +filtrar_series(criterios) list
    }

    class GestorFavoritos {
        -favoritos: list
        +agregar_favorito(Serie)
        +listar_favoritos() list
        +guardar_local()
    }

    class MotorRecomendacion {
        -catalogo: Catalogo
        +hacer_mini_test() dict
        +generar_match(preferencias) Serie
    }

    class ConsolaUI {
        -motor: MotorRecomendacion
        -favoritos: GestorFavoritos
        +__init__(MotorRecomendacion, GestorFavoritos)
        +iniciar_aplicacion()
        +mostrar_menu_principal()
        +ejecutar_mini_test() dict
        +imprimir_tarjeta_serie(Serie)
    }
```